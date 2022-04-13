<template>
  <section class="chat-layout">

    <div class="chat-leftbar">
      <div class="chat-left-headbar">
        <div class="row align-items-center">
          <div class="col-9">
            <ul class="list-unstyled mb-0">
              <li class="media">
                <img class="align-self-center mr-2"
                     src="	http://themesbox.in/admin-templates/gappa/html/light/assets/images/logo.svg"
                     alt="Generic placeholder image">
                <div class="media-body">
                  <h5 class="mb-0 mt-2">Chat</h5>
                </div>
              </li>
            </ul>
          </div>
          <div class="col-3">
            <a href="login.html" data-toggle="tooltip" data-placement="right" title="" data-original-title="Logout">
              <img src="/src/assets/icons/log-out.svg" alt="">
            </a>
          </div>
        </div>
      </div>

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

      <div class="chat-left-body">
        <div class="nav flex-column nav-pills chat-userlist" id="chat-list-tab" role="tablist"
             aria-orientation="vertical">
          <a class="nav-link active" id="chat-first-tab" data-toggle="pill" href="#chat-first" role="tab"
             aria-controls="chat-first" aria-selected="true">
            <div class="media active">
              <div class="user-status"></div>
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Emily Cook<span class="chat-timing">02:30 pm</span></h5>
                <p>Waiting for module 1 to finish...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-second-tab" data-toggle="pill" href="#chat-second" role="tab"
             aria-controls="chat-second" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>James Simeron<span class="chat-timing">Today</span></h5>
                <p>Send your CV for more info...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-third-tab" data-toggle="pill" href="#chat-third" role="tab"
             aria-controls="chat-third" aria-selected="false">
            <div class="media">
              <div class="user-status status-offline"></div>
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Lauren Gotlib<span class="badge badge-primary ml-2">5</span><span class="chat-timing">Oct 08</span>
                </h5>
                <p>Hi</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-fourth-tab" data-toggle="pill" href="#chat-fourth" role="tab"
             aria-controls="chat-fourth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Nebraska Oshivo<span class="chat-timing">Sep 25</span></h5>
                <p>Could you please send PDF?</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-fifth-tab" data-toggle="pill" href="#chat-fifth" role="tab"
             aria-controls="chat-fifth" aria-selected="false">
            <div class="media">
              <div class="user-status status-away"></div>
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Noir Ajkeban<span class="badge badge-primary ml-2">8</span> <span class="chat-timing">Sep 10</span>
                </h5>
                <p>See you at the Lunch...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-sixth-tab" data-toggle="pill" href="#chat-sixth" role="tab"
             aria-controls="chat-sixth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Will Patinson<span class="chat-timing">Sep 08</span></h5>
                <p>Where have you been?</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-seventh-tab" data-toggle="pill" href="#chat-seventh" role="tab"
             aria-controls="chat-seventh" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Simran Kaur<span class="badge badge-primary ml-2">3</span> <span class="chat-timing">Sep 07</span>
                </h5>
                <p>I sent app proposal to you.</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-eighth-tab" data-toggle="pill" href="#chat-eighth" role="tab"
             aria-controls="chat-eighth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Courtney Cox<span class="chat-timing">Sep 05</span></h5>
                <p>Please, revert on issues.</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-ninth-tab" data-toggle="pill" href="#chat-ninth" role="tab"
             aria-controls="chat-ninth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Andrew Garfield<span class="chat-timing">Aug 25</span></h5>
                <p>Your presence is awaited...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-tenth-tab" data-toggle="pill" href="#chat-tenth" role="tab"
             aria-controls="chat-tenth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Rose Witherspoon<span class="chat-timing">Aug 18</span></h5>
                <p>Fanfest is coming...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-eleventh-tab" data-toggle="pill" href="#chat-eleventh" role="tab"
             aria-controls="chat-eleventh" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Seema Roy<span class="chat-timing">Aug 11</span></h5>
                <p>Bye. Tc...</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-twelth-tab" data-toggle="pill" href="#chat-twelth" role="tab"
             aria-controls="chat-twelth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Anand Kumar<span class="badge badge-primary ml-2">2</span> <span class="chat-timing">Aug 03</span>
                </h5>
                <p>I see</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-thirteenth-tab" data-toggle="pill" href="#chat-thirteenth" role="tab"
             aria-controls="chat-thirteenth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Vladimir Jeir<span class="chat-timing">Jul 28</span></h5>
                <p>When are you coming home?</p>
              </div>
            </div>
          </a>
          <a class="nav-link" id="chat-fourtinth-tab" data-toggle="pill" href="#chat-fourtinth" role="tab"
             aria-controls="chat-fourtinth" aria-selected="false">
            <div class="media">
              <img class="align-self-center rounded-circle"
                   src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="User Image">
              <div class="media-body">
                <h5>Jessica Meir<span class="chat-timing">Jul 21</span></h5>
                <p>Hmmmm</p>
              </div>
            </div>
          </a>
        </div>
      </div>

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

        <div class="chat-head">
          <div class="row justify-content-between">
            <div class="col-6">
              <ul class="list-unstyled mb-0">
                <li class="media">
                  <div class="user-status"></div>
                  <img src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="">
                  <div class="media-body">
                    <h5>Emily Cook</h5>
                    <p class="mb-0">Online</p>
                  </div>
                </li>
              </ul>
            </div>
            <div class="col-6">
              <ul class="list-inline float-end mb-0">
                <li class="list-inline-item">
                  <button class="btn btn-primary mx-2">call</button>
                  <button class="btn btn-primary">video</button>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="chat-body">
          <div class="chat-message right">
            <div class="text">
              <span>Hello! please, let me know the status about project after school</span>
            </div>
            <div class="meta">
              <span>4:18 pm</span>
              <i class="feather icon-check ml-2"></i>
            </div>
          </div>

          <div class="chat-message left">
            <div class="text">
              <span>Hello! please, let me know the status about project after school</span>
            </div>
            <div class="meta">
              <span>4:18 pm</span>
              <i class="feather icon-check ml-2"></i>
            </div>
          </div>
        </div>

        <div class="chat-bottom">
          <div class="chat-messagebar">
            <form action="">
              <div class="input-group">
                <div class="input-group-prepend">
                  <a href="#" id="button-addonmic"><i class="feather icon-mic"></i></a>
                </div>
                <input type="text" class="form-control" placeholder="Type a message..." aria-label="Text">
                <div class="input-group-append">
                  <a href="#" class="mr-3" id="button-addonlink"><i class="feather icon-paperclip"></i></a>
                  <a href="#" id="button-addonsend"><i class="feather icon-send"></i></a>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>
import ChatWindow from "./ChatWindow.vue";

export default {
  name: "ChatApp",
  components: {
    'chat-window': ChatWindow
  }
}
</script>

<style scoped>

</style>