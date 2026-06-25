<template>
    <div class="d-flex justify-content-center mt-5">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger mt-2 mb-2" role="alert">
                    {{ message }}
                </div>

                <div class="form-floating mb-3">
                    <input type="email" class="form-control" v-model="formdata.email" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.name" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" v-model="formdata.password" id="floatingPassword"
                        placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating">
                    <select class="form-select" v-model="formdata.role" id="floatingSelect"
                        aria-label="Floating label select example">

                        <option value="customer">Customer</option>
                        <option value="professional">Professional</option>

                    </select>
                    <label for="floatingSelect">Role</label>
                </div>
                <div class="d-flex justify-content-center mt-3">
                    <button class="btn btn-primary" @click="register">Register</button>
                </div>

            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: "RegisterComp",
    data() {
        return {
            formdata: {
                email: "",
                name: "",
                password: "",
                role: ""

            },
            message: null
        }
    },
    methods: {
        async register() {
            try {
                const response = await fetch("http://localhost:5000/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body : JSON.stringify(this.formdata)
                })
                const data = await response.json()
                if (response.status == 200) {
                    console.log(data.message)
                    this.$router.push("/login")
                }
                else if (response.status == 409) {
                    this.message = data.message
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