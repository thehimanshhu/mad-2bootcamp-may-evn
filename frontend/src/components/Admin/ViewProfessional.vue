<template>
    <div v-if="prof">
        <div class="card mt-5 ms-5 me-5">
            <div class="card-body">
                <h1>{{ prof.name }}</h1>
                <h2>{{ prof.email }}</h2>
            </div>
        </div>
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
                        <tr v-for="pack in prof.packages" :key="pack.id">

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

    </div>
</template>

<script>

export default {
    name: "ViewProf",
    data() {
        return {
            prof: null,
            prof_id: null

        }
    },
    methods: {
        async getProfessional() {
            try {
                const response = await fetch(`http://localhost:5000/get-professional?prof_id=${this.prof_id}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },


                })
                const data = await response.json()
                if (response.status == 200) {
                    this.prof = data
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
        this.prof_id = this.$route.params.prof_id
        this.getProfessional()

    }


}

</script>