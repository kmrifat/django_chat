<template>
  <div class="chat-left-search">
    <form>
      <div class="input-group">
        <input type="search" class="form-control" placeholder="Search" aria-label="Search"
               aria-describedby="chat-left-search-btn">
        <div class="input-group-append">
          <button class="btn" type="submit" id="chat-left-search-btn">
            <img src="/src/assets/icons/search.svg" alt="">
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Search"
}
</script>

<style scoped>

</style>