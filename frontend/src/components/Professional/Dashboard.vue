<template>
    <div>
        <h1>{{message}}</h1>
    </div>
    
</template>

<script>


export default  {
    name: "ProfDash",
    data() {
        return {
            message: null
           
        }
    },
    methods:{
       async greet() {
            try {
                const response = await fetch("http://localhost:5000/prof-greet", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json"
                    },     
                })
                const data = await response.json()
                if (response.status == 200) {
                   this.message= data.message
                }   
            }
            catch (error) {
                console.log(error.message)
            }
        }
    },
    mounted(){
        this.greet()
    }


}

</script>