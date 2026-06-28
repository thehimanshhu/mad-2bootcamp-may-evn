<template>
    <Navbar></Navbar>


    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            Professional
        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="prof in prof_list" :key="prof.id">

                        <td>{{ prof.name }}</td>
                        <td>{{ prof.email }}</td>
                        <td>
                            <router-link :to="`/view-professional/${prof.id}`" class="btn btn-primary">View</router-link>
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </div>

    <div class="card mt-5 ms-5 me-5 mb-3">
        <div class="card-header">
            Customer
        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>

                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="cust in cust_list" :key="cust.id">

                        <td>{{ cust.name }}</td>
                        <td>{{ cust.email }}</td>
                        <td></td>
                    </tr>

                </tbody>
            </table>
        </div>
    </div>

</template>

<script>
import Navbar from '../Navbar.vue';

export default {
    name: "AdminDash",
    data() {
        return {
            prof_list: null,
            cust_list: null

        }
    },
    components: {
        Navbar
    },
    methods: {
        async listProfessionals() {
            try {
                const response = await fetch("http://localhost:5000/list-professionals", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },


                })
                const data = await response.json()
                if (response.status == 200) {
                    this.prof_list = data
                }
                else if (response.status == 401) {
                    this.message = data.message
                    this.$router.push("/login")
                }
                else if (response.status == 403) {
                    this.message = data.message
                    this.$router.push("/login")
                }
                else if (response.status == 404) {
                    this.message = data.message
                }
            }
            catch (error) {
                console.log(error.message)
            }
        },
        async listCustomers() {
            try {
                const response = await fetch("http://localhost:5000/list-customers", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },

                })
                const data = await response.json()
                if (response.status == 200) {
                    this.cust_list = data
                }
                else if (response.status == 401) {
                    this.message = data.message
                }
                else if (response.status == 404) {
                    this.message = data.message
                }
            }
            catch (error) {
                console.log(error.message)
            }
        }
    },
    mounted() {
        this.listProfessionals()
        this.listCustomers()
    }


}

</script>