import axios from "axios"
import store from './store/index'

console.log(import.meta.env)

const instance = axios.create({
    baseURL: import.meta.env.VITE_APP_API_URL
})

instance.interceptors.request.use(
    (config) => {
        if (store.state.token) {
            config.headers['Authorization'] = `Bearer ${store.state.token}`
        }
        return config
    }
)

instance.interceptors.request.use(config => {
    // app.$Progress.start();
    return config
}, (error) => {
    // app.$Progress.fail();
    return Promise.reject(error);
})

instance.interceptors.response.use(response => {
    // app.$Progress.finish()
    return response
}, (error) => {
    // app.$Progress.fail();
    return Promise.reject(error);
})

export default instance;