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

      <h1 class="mt-5 text-black-50 mb-5">Incoming call from {{ displayUser.name }}</h1>
      <button type="button" @click="answerCall" class="btn btn-lg btn-success rounded-pill px-5 me-3">Answer</button>
      <button type="button" @click="rejectCall" class="btn btn-lg btn-danger rounded-pill px-5">Reject</button>
    </div>

    <div v-if="callingStatus === 'connected'">
      <h1>Connected video call</h1>
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
      this.call = this.peer.call(this.remote_peer_id, stream)
      this.call.on('stream', this.streamRemoteCall)
    },

    streamRemoteCall(remoteStream) {
      this.callingStatus = 'connected'
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

</style>