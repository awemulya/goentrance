  <template>
  <v-list>
    <v-subheader>Units</v-subheader>

   <v-list-tile v-for="item in units" :key="item.title" :to="{path: '#'}">
     <v-list-tile-action>
              <v-icon>Book</v-icon>
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
    units: {
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
