<template>
    <Navbar></Navbar>


    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h4>Packages</h4>
                <router-link to="/create-package" class="btn btn-warning ms-auto">Create Package</router-link>
            </div>

        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="pack in pack_list" :key="pack.id">

                        <td>{{ pack.name }}</td>
                        <td>{{ pack.price }}</td>
                        <td>
                            <router-link class="btn btn-warning" :to="`/view-package/${pack.id}`">View</router-link>
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </div>


</template>

<script>
import Navbar from '../Navbar.vue';

export default {
    name: "ProfDash",
    data() {
        return {
            pack_list: null,


        }
    },
    components: {
        Navbar
    },
    methods: {
        async listPackages() {
            try {
                const response = await fetch("http://localhost:5000/list-packages", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },


                })
                const data = await response.json()
                if (response.status == 200) {
                    this.pack_list = data
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

    },
    mounted() {
        this.listPackages()

    }


}

</script>