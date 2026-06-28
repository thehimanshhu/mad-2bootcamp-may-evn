<template>
    <div class="d-flex justify-content-center mt-5">
        <div class="card" style="width: 23rem;">
            <div class="card-body">
                <div class="d-flex gap-3">
                    <div class="form-check">
                        <input class="form-check-input" type="radio" v-model="formdata.query_type" value="prof"
                            name="radioDefault" id="radioDefault1">
                        <label class="form-check-label" for="radioDefault1">
                            Prfesssional
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="radioDefault" v-model="formdata.query_type"
                            value="cust" id="radioDefault2">
                        <label class="form-check-label" for="radioDefault2">
                            Customer
                        </label>
                    </div>
                </div>
                <div class="d-flex gap-4 mt-3">
                    <div class="form-floating ">
                        <input type="email" class="form-control" v-model="formdata.query" id="floatingInput"
                            placeholder="name@example.com">
                        <label for="floatingInput">Search</label>
                    </div>
                    <button class="btn btn-primary" @click="search">Search</button>

                </div>
            </div>
        </div>
    </div>
    
    <div v-if="professionals" class="card mt-5 ms-5 me-5 mb-5">
        <div class="card-header">Professional</div>
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
                    <tr v-for="prof in professionals" :key="prof.id">

                        <td>{{ prof.name }}</td>
                        <td>{{ prof.email }}</td>
                        <td>
                            <router-link :to="`/view-professional/${prof.id}`"
                                class="btn btn-primary">View</router-link>
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </div>
    <div v-if="customers" class="card mt-5 ms-5 me-5 mb-5">
        <div class="card-header">Customer</div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="prof in customers" :key="prof.id">

                        <td>{{ prof.name }}</td>
                        <td>{{ prof.email }}</td>
                        <td>
                        
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </div>
</template>

<script>

export default {
    name: "SearchComp",
    data() {
        return {
            formdata: {
                query_type: "",
                query: ""
            },
            professionals: null,
            customers: null
        }
    },
    methods: {
        async search() {
            this.professionals = null
            this.customers = null   
            try{
                const response= await fetch("http://localhost:5000/search" , {
                    method:"POST",
                    headers :{
                        "Content-Type" : "application/json",
                        "Authentication-Token" : localStorage.getItem("token")
                    },
                    body : JSON.stringify(this.formdata)
                })
                const data = await response.json()
                if (response.status==200){
                    if(this.formdata.query_type=="prof") {
                        this.professionals = data
                    }
                    else if(this.formdata.query_type=="cust") {
                        this.customers = data
                    }
                }
                else if (response.status == 401) {
                    this.$router.push("/login")
                }
                else if (response.status == 403) {
                    this.$router.push("/login")
                }
            }
            catch(error){
                console.log(error.message)
            }
            
        }
    }

}
</script>