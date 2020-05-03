<template>

    <div>
        <form action="" @submit.prevent="mounted()">
        <div class="col-sm-6">
            <input v-model="category" category="" type="text" class="form-control">
            <button type="submit" name="button">Submit</button>
        </div>
        </form>   
        <table class="table table-striped mt-4">
        <thead>
        <tr>
            <th scope="col">name</th>
            <th scope="col">category</th>
            <th scope="col">language</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="input in directory.edges" :key="input.id">
            <td>{{ input.node.postName }}</td>
            <td>{{ input.node.postCategory.titleName }}</td>
            <td>{{ input.node.postLanguage.cityName }}</td>
        </tr>
        </tbody>
        </table>
    </div>

</template>

<script>
  import axios from 'axios'
  export default{
  	name: 'PostData',
    data(){
      return {
        category: '',
      	directory: []
      }
    },
    methods: {
        async mounted () {
            try {
                var result = await axios({
                    method: 'POST',
                    url: 'http://127.0.0.1:8000/graphql/',
                    data: {
                        query: `
                        {
                            allPosts(postCategory_CategoryName: "`+this.category+`") {
                                edges {
                                    node {
                                        id
                                        postName
                                        postCategory {
                                            categoryName
                                        }
                                        postLanguage {
                                            languageName
                                        }   
                                    }
                                }
                            }
                        }
                        `
                            }
                        })
                        this.directory = result.data.data.allPosts
                        } catch (error) {
                            console.error(error)
                        }
        }
    }

  }
</script>

<style scoped>
</style>