<template>
    <Navbar></Navbar>


    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h4>Packages</h4>
           
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
                    <tr v-for="p in pack_list" :key="p.id">

                        <td>{{ p.name }}</td>
                        <td>{{ p.price }}</td>
                        <td>
                            <router-link class="btn btn-warning" :to="`/book-package/${p.id}`">Book</router-link>
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </div>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h4>Bookings</h4>

            </div>

        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>
                        <th scope="col">Prfessional Name</th>
                        <th scope="col">Professional Email</th>
                        <th scope="col">Package Name</th>
                        <th scope="col">Date</th>
                        <th scope="col">Time</th>

                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="booking in bookings" :key="booking.id">

                        <td>{{ booking.prof_name }}</td>
                        <td>{{ booking.prof_email }}</td>
                        <td>{{ booking.package_name }}</td>
                        <td>{{ booking.date }}</td>
                        <td>{{ booking.time }}</td>

                        <td>

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
    name: "CustDash",
    data() {
        return {
            bookings: null,
            pack_list : null

        }
    },
    components: {
        Navbar
    },
    methods: {
        async listPackages() {
            try {
                const response = await fetch("http://localhost:5000/get-packages", {
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
        async getBookings() {
            try {
                const response = await fetch("http://localhost:5000/get-bookings", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },


                })
                const data = await response.json()
                if (response.status == 200) {
                    this.bookings = data
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
        this.getBookings()

    }


}

</script>