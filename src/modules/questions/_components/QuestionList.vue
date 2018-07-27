  <template>
  <v-list>
    <v-subheader>Questions</v-subheader>

   <v-list-tile v-for="question in questions" :key="question.id">
     <v-list-tile-action>
              <v-icon>Book</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title> {{question.question}}</v-list-tile-title>
            </v-list-tile-content>
   </v-list-tile>
  </v-list>
  </template>

<script>

export default {
  name: 'QuestionList',
  components: {
  },
  props: {
    questions: {
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
