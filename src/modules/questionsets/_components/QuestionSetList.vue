  <template>
  <v-list>
    <v-subheader>Question Sets</v-subheader>

   <v-list-tile v-for="set in question_sets" :key="set.title" :to="{path: '#'}">
     <v-list-tile-action>
              <v-icon>Book</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{set.name}}, {{set.type}}</v-list-tile-title>
            </v-list-tile-content>
   </v-list-tile>
  </v-list>
  </template>

<script>

export default {
  name: 'QuestionSetList',
  components: {
  },
  props: {
    question_sets: {
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
