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
      <button class="btn btn-lg btn-success rounded-pill px-5 me-3">Answer</button>
      <button class="btn btn-lg btn-danger rounded-pill px-5">Reject</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Receiver",
  data() {
    return {
      displayUser: {
        username: '',
        name: '',
        photo: 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png'
      }
    }
  },
  mounted() {
    this.displayUser = JSON.parse(this.$route.query.display)
  }
}

</script>

<style scoped>

</style>