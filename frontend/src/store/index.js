import {createStore} from "vuex";
import createPersistedState from 'vuex-persistedstate';
import {Peer} from "peerjs";

const store = createStore({
    state: {
        activeUser: null,
        token: null,
        peer_id: null,
        active_message: null
    },
    plugins: [createPersistedState()],
    mutations: {
        UPDATE_USER(state, payload) {
            state.activeUser = payload
        },
        SET_TOKEN(state, payload) {
            state.token = payload
        },
        SET_PEER(state, payload) {
            state.peer_id = payload
        },
        SET_ACTIVE_MESSAGE(state, payload) {
            state.active_message = payload
        }
    },
    actions: {
        clearState(context) {
            context.commit('UPDATE_USER')
            context.commit('SET_TOKEN')
        },
        generatePeerId(context) {
            const peer = new Peer()
            peer.on('open', (id) => {
                context.commit('SET_PEER', id)
            })
        }
    }
})

export default store