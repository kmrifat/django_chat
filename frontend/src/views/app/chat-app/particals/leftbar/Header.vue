<template>
  <div class="chat-left-headbar">
    <div class="row align-items-center">
      <div class="col-9">
        <ul class="list-unstyled mb-0">
          <li class="media">
            <img class="align-self-center mr-2"
                 src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/logo.svg"
                 alt="Generic placeholder image">
            <div class="media-body">
              <h5 class="mb-0 mt-2"> {{ $store.state.activeUser.name }}</h5>
            </div>
          </li>
        </ul>
      </div>
      <div class="col-3">
        <a @click.prevent="logout" href="/logout" data-toggle="tooltip" data-placement="right" title=""
           data-original-title="Logout">
          <img src="/src/assets/icons/log-out.svg" alt="">
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../../../../../axios";

export default {
  name: "Header",
  methods: {
    async logout() {
      await axios.post('logout/').then(response => {
        this.$store.dispatch('clearState')
        this.$router.replace('/')
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>