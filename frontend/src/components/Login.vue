<template>
    <div class="d-flex justify-content-center" width="20rem;">
    <div class="form-floating mb-3">
        <input type="email" class="form-control" v-model="formdata.email" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
        <input type="password" class="form-control" v-model="formdata.pass" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Password</label>
    </div>
    <button class="btn btn-primary" @click="login">Login</button>
    </div>
</template>

<script>
export default{
    name : "LoginComp",
    data(){
        return {
            formdata : {
                email:"",
                pass:"",
                name : "himanshu"
            }
        }
    },
    methods : {
        login(){
            console.log("data is: " , this.formdata)
           
        }
    }
}
</script>