<template>
  <div class="chat-left-body">
    <div class="nav flex-column nav-pills chat-userlist" id="chat-list-tab" role="tablist"
         aria-orientation="vertical">
      <a v-for="user in users" class="nav-link" :class="selected_user == user ? 'active' : ''" id="chat-first-tab"
         @click="setSelectedUser(user)">
        <div class="media active">
          <div v-if="user.online" class="user-status"></div>
          <img class="align-self-center rounded-circle"
               src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
          <div class="media-body">
            <h5>{{ user.name }} <span class="chat-timing">{{ user.messages[0]?.date_time }}</span></h5>
            <p>{{ user.messages ? user.messages[0].text : user.status }}</p>
          </div>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
import {store} from "../../store";

export default {
  name: "UserList",
  data() {
    return {
      users: store.users,
      selected_user: store.selected_user
    }
  },
  methods: {
    setSelectedUser(user) {
      this.$emit('update:modelValue', user)
    }
  }
}
</script>

<style scoped>

</style>