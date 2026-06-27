import { createRouter, createWebHistory } from "vue-router"
import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Register from "./components/Register.vue"
import AdminDashboard from "./components/Admin/Dashboard.vue"
import ProfDashboard from "./components/Professional/Dashboard.vue"
import CustDashboard from "./components/Customer/Dashboard.vue"
import CreatePackage from "./components/Professional/CreatePackage.vue"
import ViewPackage from "./components/Professional/ViewPackage.vue"

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

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router