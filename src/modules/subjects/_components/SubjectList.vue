  <template>
  <v-list>
    <v-subheader>Subjects</v-subheader>

   <v-list-tile v-for="item in subjects" :key="item.title" :to="{path: '/unit/' + item.id}">
     <v-list-tile-action>
              <v-icon :color="item.id ? 'teal' : 'grey'">mdi-book-open</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{item.name}}</v-list-tile-title>
            </v-list-tile-content>
   </v-list-tile>
  </v-list>
  </template>

<script>
// import SubjectListElement from './SubjectListElement'

export default {
  name: 'SubjectList',
  components: {
    // SubjectListElement
  },
  props: {
    subjects: {
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
