  <template>
  <div class="text-md-center">
    <v-subheader class="text-xs-center mb-3">Units</v-subheader>
    <v-flex class="text-xs-center">
    <v-expansion-panel
      v-model="panel"
      expand
    >
      <v-expansion-panel-content
        v-for="item in units" v-bind:key="item.title">
        <div slot="header"  color="white lighten-4" >{{item.name}} ({{item.unit_chapters.length}}) Chapters</div>
        <v-card v-for="chapter in item.unit_chapters" v-bind:key="chapter"  color="white lighten-4">
            <v-icon color="teal" medium>mdi-minus</v-icon>
          <v-btn :to="{path: '/question-sets/' + chapter.id}">
          {{chapter.name}}
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
  data: () => ({
    panel: [],
    link: ''
  }),
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
