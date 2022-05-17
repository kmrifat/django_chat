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
      <button class="btn btn-lg btn-danger rounded-pill">Cancel Call</button>
    </div>
  </div>


</template>

<script>
import axios from "../../../axios";

export default {
  name: "Sender",
  data() {
    return {
      displayUser: {
        username: '',
        name: '',
        photo: 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png'
      },
      user: null
    }
  },
  methods: {
    startCall() {
      let data = {
        receiver: this.$route.params.receiver,
        sender: this.$route.params.username
      }
      console.log(this.$route.params)
      console.log(data)
      axios.post('authentication/start-call/', data).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error.response)
      })
    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
    this.startCall()
  }
}
</script>

<style scoped>


</style>