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
      <h2 class="mt-5 text-black-50 mb-5">Calling <strong>{{ displayUser.name }}</strong> .....</h2>
      <button type="button" @click="cancelCall" class="btn btn-lg btn-danger rounded-pill">Cancel Call</button>
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
      conn: null
    }
  },
  methods: {
    startCall() {
      let data = {
        receiver: this.$route.params.receiver,
        sender: this.$route.params.username,
        peer_id: this.$store.state.peer_id
      }
      console.log(this.$route.params)
      console.log(data)
      axios.post('authentication/start-call/', data).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error.response)
      })
    },
    ready() {
      this.conn.on('data', (data) => {
        console.log("Data recieved", data)
      })

      this.conn.on('close', () => {
        console.log("Connection reset Awaiting connection")
        this.conn = null
      })
    },
    cancelCall() {

    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.peer = new Peer()
    this.peer.on('open', (id) => {
      this.peer_id = id;
      this.$store.commit('SET_PEER', id)
    })

    this.peer.on('connection', (conn) => {
      this.conn = conn
      console.log("hello connection", conn.peer)
      this.ready()

    })

    this.peer.on('disconnected', () => {
      console.log('Connection lost. Please reconnect');
    })

    this.peer.on('close', () => {
      console.log('Connection destroyed');
    })

    this.startCall()
  }
}
</script>

<style scoped>


</style>