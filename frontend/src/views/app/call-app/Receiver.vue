<template>
  <div style="height: 100vh" class="d-flex justify-content-center align-items-center">
    <div class="text-center align-self-center" v-show="callingStatus === 'calling'">
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
        <i class="fa-solid fa-phone" style="transform: rotate(133deg)"></i> Reject</button>
    </div>

    <div v-show="callingStatus === 'connected'">
      <video ref="localVideo" src="" id="localVideo" autoplay="autoplay" muted></video>

      <video ref="remoteVideo" src="" id="remoteVideo" autoplay muted></video>

      <div class="call-controls text-center align-self-center p-3 bg-primary bg-opacity-10">
        <button class="btn btn-lg btn-secondary rounded-circle mx-1"><i class="fa-solid fa-microphone"></i></button>
        <button class="btn btn-lg btn-primary rounded-circle mx-1"><i class="fa-solid fa-video"></i></button>
        <button class="btn btn-lg btn-danger rounded-circle mx-1"><i class="fa-solid fa-phone"
                                                                     style="transform: rotate(133deg)"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
import Peer from "peerjs";

export default {
  name: "Receiver",
  data() {
    return {
      peer: null,
      conn: null,
      call: null,
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
    },

    answerCall() {
      this.getUserMedia({video: true, audio: true}, this.streamCall, (error) => {
        console.error(error)
      })
    },

    streamCall(stream) {
      this.callingStatus = 'connected'
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

    rejectCall() {
      this.conn = this.peer.connect(this.remote_peer_id)
      this.conn.on('open', () => {
        this.conn.send({
          status: 400,
          statusText: 'rejected',
          data: `${this.$store.state.activeUser.name} Has declined your call`
        })
      })
    },
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.remote_peer_id = this.$route.query.peer_id
    this.initializePeer()


  }
}

</script>

<style scoped>
.rotate-90{
  transform: rotate(45deg);
}
</style>