<template>
    <div id="app">
        <div v-for="survey in surveys" :key="survey.id">
            <div>
              {{ survey.title }}
            </div>
            <div>
              {{ survey.comment }}
            </div>
            <div v-for="choice in surveys.choice">
                <a v-bind:href="choice ">vote for {{ choice }}</a>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'app',
    data: function () {
        return {
            surveys: []
        }
    },
    methods: {
        loadSurveys: function () {
        axios.get('api/surveys').then((response) => {
            this.surveys = response.data
          }, (err) => {
            console.log(err)
          })
    }
    },
    mounted: function () {
        this.loadSurveys()
    }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

h1, h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>
