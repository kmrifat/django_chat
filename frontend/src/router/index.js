import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: '/', component: () => import('../views/auth/Layout.vue'),
        children: [
            {path: '', component: () => import('../views/auth/Login.vue')},
            {path: 'registration', component: () => import('../views/auth/Registration.vue')},
            {path: 'forget-password', component: () => import('../views/auth/ForgetPassword.vue')},
            {path: 'reset-password', component: () => import('../views/auth/ResetPassword.vue')}
        ]
    },
    {
        path: '/app', component: () => import('../views/app/Layout.vue'),
        children: [
            {path: '', component: () => import('../views/app/chat-app/ChatApp.vue')}
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router