import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import Toast, {POSITION} from 'vue-toastification';
import 'vue-toastification/dist/index.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(store).use(router, axios).use(Toast, {position: POSITION.TOP_CENTER}).mount('#app')