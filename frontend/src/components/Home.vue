<template>
    <div>
        <h1>Welcome to My app</h1>
        <div class="d-flex justify-content-center gap-2">
            <router-link to="/login" class="btn btn-primary" >
                Login
            </router-link>
            <router-link to="/register" class="btn btn-warning">
                Register
            </router-link>
        </div>
    </div>
    
</template>

<script>


export default  {
    name: "HomeComp",
    data() {
        return {
            formdata: {
                email: "",
                pass: "",
                name: "himanshu"
            },
           
        }
    },



}

</script>