import {createStore} from "vuex";
import createPersistedState from 'vuex-persistedstate';

const store = createStore({
    state: {
        activeUser: null,
        token: null
    },
    plugins: [createPersistedState()],
    mutations: {
        UPDATE_USER(state, payload) {
            state.activeUser = payload
        },
        SET_TOKEN(state, payload) {
            state.token = payload
        }
    },
    actions: {
        clearState(context) {
            context.commit('UPDATE_USER')
            context.commit('SET_TOKEN')
        }
    }
})

export default store