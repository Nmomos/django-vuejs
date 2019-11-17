<template>
  <div id="app">
    <v-btn @click="getHedgeHogData">test</v-btn>
  </div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import router from "../../router";
export default {
  name: "HedgeHogs",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },
    getHedgeHogData() {
      axios
        .get("http://localhost:8000/api/hedgehogs/")
        .then(res => {
          console.log(res.data[0]);
          console.log(res.data[1]);
          console.log(res.data[2]);
        })
        .catch(e => {
          Swal.fire({
            type: "error",
            title: "error",
            text: "ERROR"
          });
        });
    }
  }
};
</script>
