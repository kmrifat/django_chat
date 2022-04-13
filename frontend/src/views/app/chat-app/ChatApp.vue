<template>
  <section class="chat-layout">

    <div class="chat-leftbar">
      <left-header></left-header>

      <search-bar></search-bar>

      <user-list v-model="selected_user"></user-list>


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
        <message-window :selected_user="selected_user"></message-window>
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
      selected_user: store.selected_user
    }
  },
  methods: {}
}
</script>

<style scoped>

</style>