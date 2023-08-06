import {createRouter, createWebHistory} from 'vue-router'

import HomeView from '../views/HomeView.vue'
import SignUp from "@/views/SignUp.vue";
import ConfirmEmail from "@/views/ConfirmEmail.vue";
import EmailConfirmed from "@/views/EmailConfirmed.vue";
import SignIn from "@/views/SignIn.vue";
import Terms from "@/views/Terms.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp,
    },
    {
        path: '/sign-in',
        name: 'SignIn',
        component: SignIn,
    },
    {
        path: '/terms',
        name: 'Terms',
        component: Terms
    },
    {
        path: '/confirm-email',
        name: 'ConfirmEmail',
        component: ConfirmEmail,
    },
    {
        path: '/email-confirmed',
        name: 'EmailConfirmed',
        component: EmailConfirmed,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
