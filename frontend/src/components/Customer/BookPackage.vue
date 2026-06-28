<template>
    <div class="text-center mt-5">
        <h1>Book Package</h1>
    </div>
    <div class="d-flex justify-content-center mt-5">

        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger" role="alert">
                    {{ message }}
                </div>

                <div class="form-floating mb-3">
                    <input type="date" class="form-control" v-model="formdata.date" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Date</label>
                </div>
                <div class="form-floating">
                    <input type="time" class="form-control" v-model="formdata.time" id="floatingPassword"
                        placeholder="Password">
                    <label for="floatingPassword">Time</label>
                </div>
                <div class="d-flex justify-content-center mt-2">
                    <button class="btn btn-primary" @click="book">Book</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "BookPackage",
    data() {
        return {
            formdata: {
                date : "",
                time : ""
            },
            message: null
        }
    },
    methods: {
        async book() {
            try {
                const response = await fetch(`http://localhost:5000/book-package?pack_id=${this.pack_id}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token" : localStorage.getItem("token")
                    },
                    body : JSON.stringify(this.formdata)
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.$router.push("/customer/dashboard")
                }
                else if (response.status == 401) {
                    this.$router.push("/login")
                }
                else if (response.status == 403) {
                    this.$router.push("/login")
                }
                else if (response.status == 400) {
                    this.message = data.message
                } 
            }
            catch (error) {
                console.log(error.message)
            }
        }
    },
    mounted(){
        this.pack_id = this.$route.params.pack_id
    }
}
</script>