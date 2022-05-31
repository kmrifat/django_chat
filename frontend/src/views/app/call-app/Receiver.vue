<template>
  <div style="height: 100vh" class="d-flex justify-content-center align-items-center">
    <div class="text-center align-self-center" v-show="callingStatus === 'calling'">
<!--      <audio src="/public/sounds/iphone-ringtone-47958.mp3" controls loop autoplay></audio>-->
      <center>
        <div class="pulse">
          <img height="250" :src="displayUser.photo"
               class="rounded-circle"
               alt="">
        </div>
      </center>

      <h1 class="mt-5 text-black-50 mb-5">Incoming call from <strong>{{ displayUser.name }}</strong></h1>
      <button type="button" @click="answerCall" class="btn btn-lg btn-success rounded-pill px-5 me-3">
        <i class="fa-solid fa-phone"></i> Answer
      </button>
      <button type="button" @click="rejectCall" class="btn btn-lg btn-danger rounded-pill px-5">
        <i class="fa-solid fa-phone" style="transform: rotate(133deg)"></i> Reject
      </button>
    </div>

    <div v-show="callingStatus === 'connected'">
      <video ref="localVideo" src="" id="localVideo" autoplay="autoplay"></video>

      <video ref="remoteVideo" src="" id="remoteVideo" autoplay></video>

      <div class="call-controls text-center align-self-center p-3 bg-primary bg-opacity-10">
        <mic-button :click-callback="toggleLocalAudio"></mic-button>
        <video-button :click-callback="toggleLocalVideo"></video-button>
        <button @click="rejectCall" class="btn btn-lg btn-danger rounded-circle mx-1">
          <i class="fa-solid fa-phone" style="transform: rotate(133deg)"></i>
        </button>
      </div>
    </div>

    <div v-if="callingStatus === 'rejected'">
      <h1>Call Rejected, closing the window</h1>
    </div>
  </div>
</template>

<script>
import Peer from "peerjs";
import MicButton from "../../../components/buttons/MicButton.vue";
import VideoButton from "../../../components/buttons/VideoButton.vue";
import axios from "../../../axios";

export default {
  name: "Receiver",
  components: {
    'mic-button': MicButton,
    'video-button': VideoButton
  },
  data() {
    return {
      socket: null,
      peer: null,
      conn: null,
      call: null,
      localStream: null,
      remote_peer_id: null,
      displayUser: {
        username: '',
        name: '',
        photo: 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png'
      },
      callingStatus: 'calling', // there will three status : 101 calling, 400 => rejected, 200 => connected
      getUserMedia: navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia
    }
  },
  methods: {
    initializePeer() {
      this.peer = new Peer()
      this.peer.on('open', (id) => {
        this.peer_id = id;
        console.log("My peer id")
        this.$store.commit('SET_PEER', id)
      })

      this.peer.on('connection', (conn) => {
        conn.on('data', (data) => {
          console.log("recieved", data)
        })
      })
      this.initializeWebSocket(this.remote_peer_id)
    },

    answerCall() {
      this.getUserMedia({video: true, audio: true}, this.streamCall, (error) => {
        console.error(error)
      })
    },

    streamCall(stream) {
      this.callingStatus = 'connected'
      this.localStream = stream
      this.call = this.peer.call(this.remote_peer_id, stream)
      this.call.on('stream', this.streamRemoteCall)
      this.$refs.localVideo.srcObject = stream
      this.$refs.localVideo.play()
    },

    streamRemoteCall(remoteStream) {
      this.$refs.remoteVideo.srcObject = remoteStream
      this.$refs.remoteVideo.play()
      console.log("remote stream")
    },

    toggleLocalVideo() {
      this.localStream.getTracks().forEach((track) => {
        if (track.readyState === 'live' && track.kind === 'video') {
          track.enabled = !track.enabled;
        }
      })
    },

    toggleLocalAudio() {
      this.localStream.getTracks().forEach((track) => {
        if (track.readyState === 'live' && track.kind === 'audio') {
          track.enabled = !track.enabled;

        }
      })
    },

    rejectCall() {
      let data = {
        receiver: this.displayUser.username,
        sender: this.$route.params.username,
        peer_id: this.remote_peer_id
      }
      axios.post('end-call/', data).then(response => {
        console.log(response)
      }).catch(err => {
        console.log(err)
      })
    },

    initializeWebSocket(peer_id) {
      this.socket = new WebSocket(`${import.meta.env.VITE_WS_ENDPOINT}ws/message/${peer_id}/`)
      this.socket.onmessage = (event) => {
        let message = JSON.parse(event.data);
        switch (message.status) {
          case 'end_call':
            this.endCall()
            break
        }
        console.log(message)
      }
    },

    endCall() {
      this.callingStatus = 'rejected'
      setTimeout(() => {
        window.close()
      }, 2000)
    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.remote_peer_id = this.$route.query.peer_id
    this.initializePeer()
  },
  beforeMount() {
    window.addEventListener('beforeunload', ev => {
      this.endCall()
    })
  }
}

</script>

<style scoped>
.rotate-90 {
  transform: rotate(45deg);
}
</style>