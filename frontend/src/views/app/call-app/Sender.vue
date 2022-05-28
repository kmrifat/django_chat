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
      <h2 class="mt-5 text-black-50 mb-5">Calling <strong>{{ displayUser.name }}</strong> .....</h2>
      <button type="button" @click="cancelCall" class="btn btn-lg btn-danger rounded-pill px-5">
        <i class="fa-solid fa-phone" style="transform: rotate(133deg)"></i> Cancel Call
      </button>
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
import axios from "../../../axios";
import {Peer} from "peerjs"

export default {
  name: "Sender",
  data() {
    return {
      displayUser: {
        username: '',
        name: '',
        photo: 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png'
      },
      peer_id: null,
      user: null,
      peer: null,
      conn: null,
      call: null,
      callingStatus: 'calling', // there will three status : 101 calling, 400 => rejected,200 => connected
      getUserMedia: navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia
    }
  },
  methods: {
    initializePeer() {
      this.peer = new Peer()
      this.peer.on('open', (id) => {
        this.peer_id = id
        this.startCall()
        console.log("My peer id", id)
        console.log("My store id", this.$store.state.peer_id)
      })

      this.peer.on('connection', this.handleConnection)

      this.peer.on('call', this.handleCall)
    },

    handleConnection(conn) {
      this.conn = conn
      this.conn.on('data', (data) => {
        console.log("Received", data)
      })
    },

    handleCall(call) {
      this.call = call
      this.getUserMedia({video: true, audio: true}, this.streamCall)
    },

    streamCall(stream) {
      this.callingStatus = 'connected'
      this.call.answer(stream)
      this.$refs.localVideo.srcObject = stream
      this.$refs.localVideo.play()
      this.call.on('stream', this.streamRemoteCall)
    },

    streamRemoteCall(remoteStream) {
      this.$refs.remoteVideo.srcObject = remoteStream
      this.$refs.remoteVideo.play()
      console.log("remote stream")
    },

    startCall() {
      let data = {
        receiver: this.$route.params.receiver,
        sender: this.$route.params.username,
        peer_id: this.peer_id
      }
      console.log(this.$route.params)
      console.log(data)
      axios.post('start-call/', data).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error.response)
      })
    },
    cancelCall() {
      console.log(this.conn)
    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.initializePeer()

    // this.startCall()
  },
  beforeMount() {
    window.addEventListener('beforeunload', ev => {
      if (this.peer_id)
        ev.preventDefault()
      ev.returnValue = ""
    })
  }
}
</script>

<style scoped>


</style>