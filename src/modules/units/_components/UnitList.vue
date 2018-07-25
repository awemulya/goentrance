  <template>
  <div class="text-md-center">
    <v-subheader class="text-xs-center mb-3">Units</v-subheader>
    <v-flex class="text-xs-center">
    <v-expansion-panel
      v-model="panel"
      expand
      dark
    >
      <v-expansion-panel-content
        v-for="item in units" v-bind:key="item.title">
        <div slot="header"  color="blue lighten-4" >{{item.name}}</div>
        <v-card v-for="chapter in item.unit_chapters" v-bind:key="chapter"  color="blue lighten-4">
            <v-icon color="black" medium>book</v-icon>
          <v-btn :to="{path: ''}">
          {{chapter}}
          </v-btn>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
    </v-flex>
    </div>
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
    },
    panel: ''
  }
}

</script>

<style scoped>

</style>
