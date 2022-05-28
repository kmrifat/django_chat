<template>
  <div style="height: 100vh" class="d-flex justify-content-center align-items-center">
    <div class="text-center align-self-center" v-if="callingStatus === 'calling'">
      <center>
        <div class="pulse">
          <img height="250" :src="displayUser.photo"
               class="rounded-circle"
               alt="">
        </div>
      </center>
      <h2 class="mt-5 text-black-50 mb-5">Calling <strong>{{ displayUser.name }}</strong> .....</h2>
      <button type="button" @click="cancelCall" class="btn btn-lg btn-danger rounded-pill">Cancel Call</button>
    </div>

    <div v-if="callingStatus === 'connected'">
      <h1>Connected video call</h1>
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
      this.call.answer(stream)
      this.call.on('stream', this.streamRemoteCall)
    },

    streamRemoteCall(remoteStream) {
      this.callingStatus = "connected"
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
      axios.post('authentication/start-call/', data).then(response => {
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
  }
}
</script>

<style scoped>


</style>