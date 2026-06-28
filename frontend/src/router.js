import { createRouter, createWebHistory } from "vue-router"
import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Register from "./components/Register.vue"
import AdminDashboard from "./components/Admin/Dashboard.vue"
import ProfDashboard from "./components/Professional/Dashboard.vue"
import CustDashboard from "./components/Customer/Dashboard.vue"
import CreatePackage from "./components/Professional/CreatePackage.vue"
import ViewPackage from "./components/Professional/ViewPackage.vue"
import ViewProfessional from "./components/Admin/ViewProfessional.vue"
import BookPackage from "./components/Customer/BookPackage.vue"
import Search from "./components/Admin/Search.vue"

const routes = [
    {
        "path": "/", component: Home
    },
    {
        "path": "/login", component: Login
    },
    {
        "path": "/register", component: Register
    },
    {
        "path": "/admin/dashboard", component: AdminDashboard
    },
    {
        "path": "/professional/dashboard", component: ProfDashboard
    },
    {
        "path": "/customer/dashboard", component: CustDashboard
    },
    {
        "path": "/create-package", component: CreatePackage
    },
    {
        "path": "/view-package/:pack_id", component: ViewPackage
    },
    {
        "path": "/view-professional/:prof_id", component: ViewProfessional
    },
    {
        "path": "/book-package/:pack_id", component: BookPackage
    },
    {
        "path": "/search", component: Search
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router