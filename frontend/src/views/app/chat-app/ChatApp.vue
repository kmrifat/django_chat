<template>
  <section class="chat-layout">

    <div class="chat-leftbar">
      <left-header></left-header>

      <search-bar></search-bar>

      <user-list v-model="selected_user" :users="users"></user-list>


      <div class="chat-menu">
        <ul class="nav nav-pills nav-justified mb-0" id="pills-tab-justified" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="pills-chat-tab-justified" data-toggle="pill" href="#pills-chat-justified"
               role="tab" aria-controls="pills-chat-justified" aria-selected="true">
              <img src="/src/assets/icons/message-circle.svg" alt="">
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="pills-addchat-tab-justified" data-toggle="pill" href="#pills-addchat-justified"
               role="tab" aria-controls="pills-addchat-justified" aria-selected="false">
              <img src="/src/assets/icons/edit-3.svg" alt="">
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="pills-profile-tab-justified" data-toggle="pill" href="#pills-profile-justified"
               role="tab" aria-controls="pills-profile-justified" aria-selected="false">
              <img src="/src/assets/icons/user.svg" alt="">
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="pills-setting-tab-justified" data-toggle="pill" href="#pills-setting-justified"
               role="tab" aria-controls="pills-setting-justified" aria-selected="false">
              <img src="/src/assets/icons/settings.svg" alt="">
            </a>
          </li>
        </ul>
      </div>

    </div>

    <div class="chat-rightbar show">
      <div class="chat-details">
        <message-window ref="messageWindow" :selected_user="selected_user"></message-window>
      </div>
    </div>

  </section>
</template>

<script>


import Header from "./particals/leftbar/Header.vue";
import Search from "./particals/leftbar/Search.vue";
import UserList from "./particals/leftbar/UserList.vue";
import MessageWindow from "./particals/rightbar/MessageWindow.vue";
import {store} from "./store";
import axios from "../../../axios";

export default {
  name: "ChatApp",
  components: {
    'left-header': Header,
    'search-bar': Search,
    'user-list': UserList,
    'message-window': MessageWindow,
  },
  data() {
    return {
      users: store.users,
      selected_user: store.selected_user,
      connection: null,
      message_connection: null
    }
  },
  watch: {
    'selected_user': {
      handler() {
        setTimeout(() => {
          this.$refs.messageWindow.scrollDown()
        }, 500)
      }
    }
  },
  methods: {
    fetchUsers() {
      axios.get('users/').then(response => {
        // store.users = response.data
        this.users = response.data
        console.log(response.data)
      }).catch(error => {
        console.log(error)
      })
    },

    openCallViewWindow(data) {
      console.log("openCallViewWindow", data)
      let routeData = this.$router.resolve({
        name: 'receiverView',
        params: {username: data.data.receiver, sender: data.data.sender},
        query: {
          display: JSON.stringify(data.display),
          peer_id: data.data.peer_id
        }
      })
      window.open(routeData.href, '_blank', 'popup,height=650,width=550,resizable=0,location=no,toolbar=no,menubar=no,resizable=no')
      // window.open(routeData.href, '_blank')
    }
  },
  mounted() {
    this.fetchUsers()
    this.$store.dispatch('generatePeerId')
  },
  created() {
    this.connection = new WebSocket(`${import.meta.env.VITE_WS_ENDPOINT}ws/notification/`)
    this.message_connection = new WebSocket(`${import.meta.env.VITE_WS_ENDPOINT}ws/message/${this.$store.state.activeUser.username}/`)

    this.connection.onmessage = (event) => {
      let message = JSON.parse(event.data).message;
      if (JSON.parse(event.data).status === 'new_user') {
        this.users.push(message)
      } else {
        this.users.filter(value => {
          if (value.username === message.username) value.online = message.online
        })
      }
    }

    this.message_connection.onmessage = (event) => {
      let eventJSON = JSON.parse(event.data)
      if (eventJSON.status === 'new_call') {
        console.log("new call")
        this.openCallViewWindow(eventJSON.message)
      } else {
        let message = JSON.parse(event.data).message
        console.log(message)
        let user = this.users.filter(value => {
          return value.username === message.sender
        })[0]
        user.messages.push(message)
        if (this.selected_user.username === user.username) {
          user.messages.filter(value => value.read = true)
        }
        this.users.splice(this.users.indexOf(user), 1)
        this.users.unshift(user)
      }
    }

    this.connection.onopen = (event) => {
      console.log("Created", event)
    }
  }
}
</script>

<style scoped>

</style>