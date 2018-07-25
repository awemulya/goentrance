<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
    >
      <v-list dense>
      <router-link to="/" tag="span" style="cursor: pointer">
        <v-list-tile @click="link">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        </router-link>
        <v-list-tile @click="link">
          <v-list-tile-action>
            <v-icon>contact_mail</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Contact</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar dark color="primary" fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Entrance</v-toolbar-title>
      <v-spacer></v-spacer>
    <v-btn icon><router-link to="/" tag="span" style="cursor: pointer">
        <v-icon>search</v-icon>
      </router-link>
      </v-btn>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>refresh</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>more_vert</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
    <v-btn color="orange darken-2" dark @click="goBack" tag="span" style="cursor: pointer">
        <v-icon dark left>arrow_back</v-icon>Back
        </v-btn>
      <v-container class="text-xs-center">
        <v-layout
          justify-center
          align-left>
          <v-flex text-xs-center>
          <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    link: ''
  }),
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  },
  props: {
    source: String
  }
}
</script>
