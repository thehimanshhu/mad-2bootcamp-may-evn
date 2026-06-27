<template>
    <div class="text-center mt-5">
        <h1>Create Package</h1>
    </div>
    <div class="d-flex justify-content-center mt-5">

        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger" role="alert">
                    {{ message }}
                </div>

                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.name" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Name</label>
                </div>
                <div class="form-floating">
                    <input type="number" class="form-control" v-model="formdata.price" id="floatingPassword"
                        placeholder="Password">
                    <label for="floatingPassword">Price</label>
                </div>
                <div class="d-flex justify-content-center mt-2">
                    <button class="btn btn-primary" @click="create">Create</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CreatePackage",
    data() {
        return {
            formdata: {
                name : "",
                price : ""
            },
            message: null
        }
    },
    methods: {
        async create() {
            try {
                const response = await fetch("http://localhost:5000/create-package", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token" : localStorage.getItem("token")
                    },
                    body : JSON.stringify(this.formdata)
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.$router.push("/professional/dashboard")
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
    }
}
</script>