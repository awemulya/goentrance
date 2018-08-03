  <template>
    <v-container fluid grid-list-md>
      <v-data-iterator
        :items="question_sets"
        :rows-per-page-items="rowsPerPageItems"
        :pagination.sync="pagination"
        content-tag="v-layout"
        hide-actions
        row
        wrap
      >
        <v-toolbar
          slot="header"
          class="mb-2"
          color="indigo darken-5"
          dark
          flat
        >
          <v-toolbar-title>Available Question Sets</v-toolbar-title>
        </v-toolbar>
        <v-flex
          slot="item"
          slot-scope="props"
          xs12
          sm6
          md4
          lg3
        >
          <v-card :to="{path: '/questions/' + props.item.id}">
            <v-card-title class="subheading font-weight-bold">{{ props.item.name }}</v-card-title>
            <v-divider></v-divider>
            <v-list dense>
              <v-list-tile>
                <v-list-tile-content>Type:</v-list-tile-content>
                <v-list-tile-content class="align-end">{{ props.item.type }}</v-list-tile-content>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-content>Questions:</v-list-tile-content>
                <v-list-tile-content class="align-end">{{ props.item.questions_count }}</v-list-tile-content>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-content>Time:</v-list-tile-content>
                <v-list-tile-content class="align-end">{{ props.item.time }}</v-list-tile-content>
              </v-list-tile>
            </v-list>
          </v-card>
        </v-flex>
      </v-data-iterator>
    </v-container>
  </template>

<script>
export default {
  name: 'QuestionSetList',
  data: () => ({
    rowsPerPageItems: [4, 8, 12],
    pagination: {
      rowsPerPage: 10
    }
  }),
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
