<template>
  <div style="height: 100vh" class="d-flex justify-content-center align-items-center">
    <div class="text-center align-self-center">
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
      remote_peer_id: null,
      displayUser: {
        username: '',
        name: '',
        photo: 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png'
      }
    }
  },
  methods: {
    answerCall() {

    },
    rejectCall() {

    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.remote_peer_id = this.$route.query.peer_id
    this.peer = new Peer(null, {
      debug: 2
    })
    this.peer.on('open', (id) => {
      this.$store.commit('SET_PEER', id)
    })
    this.peer.on('connection', (c) => {
      c.on('open', () => {
        c.send('Sender does not accept incoming connections')
        setTimeout(function () {
          c.close();
        }, 500);
      })
    })
    this.peer.on('disconnected', () => {
      console.log('Connection lost. Please reconnect');
    })

    this.peer.on('close', () => {
      this.conn = null
      console.log('Connection destroyed');
    })

    this.peer.on('error', (err) => {
      console.log(err)
    })

    this.conn = this.peer.connect(this.remote_peer_id, {
      reliable: true
    })

    this.conn.on('open', () => {
      console.log("Connected to: " + this.conn.peer);
      this.conn.send("hello world")
    })

    this.conn.on('data', (data) => {
      console.log("hello", data)
    })

    this.conn.on('close', () => {
      console.log("Connection close")
    })
  }
}

</script>

<style scoped>

</style>