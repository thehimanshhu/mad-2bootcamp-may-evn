<template>
    <div v-if="pack">
        <div class="card mt-5 ms-5 me-5">
            <div class="card-body">
                <h1>{{ pack.name }}</h1>
                <h2>{{ pack.price }}</h2>
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
                            <th scope="col">Customer Name</th>
                            <th scope="col">Customer Email</th>
                            <th scope="col">Date</th>
                            <th scope="col">Time</th>
                            
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="booking in pack.bookings" :key="booking.id">

                            <td>{{ booking.customer_name }}</td>
                            <td>{{ booking.customer_email }}</td>
                            <td>{{ booking.date }}</td>
                            <td>{{ booking.time }}</td>
                            
                            <td>

                            </td>
                        </tr>


                    </tbody>
                </table>
            </div>
        </div>

    </div>
</template>

<script>

export default {
    name: "ViewPackage",
    data() {
        return {
            pack: null,
            pack_id: null

        }
    },
    methods: {
        async getPackage() {
            try {
                const response = await fetch(`http://localhost:5000/get-package?pack_id=${this.pack_id}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },


                })
                const data = await response.json()
                if (response.status == 200) {
                    this.pack = data
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
        this.pack_id = this.$route.params.pack_id
        this.getPackage()

    }


}

</script>