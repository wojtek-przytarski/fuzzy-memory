<template>
  <div class="m-auto">

    <div id="numberFormContainer">
      <b-overlay :show="loading">
        <h5 class="text-left">Enter an integer between -100000 and 100000</h5>
        <b-input-group class="mt-3">
          <b-input v-model="number" id="numberInput" type="number" step="1" min="-100000" max="100000"
                   class="form-control" @keyup="onInputChange" @keyup.enter="onSubmit"></b-input>
          <b-input-group-append>
            <b-button variant="primary" @click="onSubmit">Button</b-button>
          </b-input-group-append>
        </b-input-group>
        <b-alert show v-if="errorDetail" variant="danger" class="p-1 mt-2 mb-1">{{ errorDetail }}</b-alert>
      </b-overlay>
    </div>

    <div id="resultBox" v-if="result.numerator">
      <h3 class="text-left">Result</h3>
      <hr>
      <div>
        <div>
          {{ result.numerator }}
        </div>
        <div class="fraction-line" v-if="result.denominator && result.denominator !== '1'"></div>
        <div v-if="result.denominator !== '1'">
          {{ result.denominator }}
        </div>
      </div>
    </div>

  </div>
</template>
<script>

import {SecondTetrationService} from "../services/second-tetration.service";

export default {
  name: 'SecondTetrationForm',
  data() {
    return {
      number: null,
      result: {
        numerator: null,
        denominator: null,
      },
      job_id: "",
      errorDetail: "",
      loading: false,
    }
  },
  methods: {
    onSubmit() {
      if (this.errorDetail || this.loading) {
        return;
      }
      this.result = {};
      this.loading = true;
      this.errorDetail = null;
      SecondTetrationService.fetch(this.number)
          .then(result => {
            this.result = result;
          })
          .catch(error => {
            this.errorDetail = error;
          }).finally(() => this.loading = false);
    },
    onInputChange() {
      if (Math.floor(this.number) != this.number) {
        this.errorDetail = "Provided number is not an integer"
      } else if (this.number < -100000 || this.number > 100000) {
        this.errorDetail = "Provided number is out of range"
      } else {
        this.errorDetail = null;
      }
    },
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#resultBox {
  text-align: center;

  border: 1px solid #0a161f;
  padding: 1em;
  border-radius: 5px;

  word-break: break-all;
}

#numberFormContainer {
  max-width: 500px;
  margin: 1em auto;
  border: 1px solid #0a161f;
  border-radius: 5px;
  padding: 1em;
}

.fraction-line {
  border-bottom: 1px solid black;
  width: 20px;
  margin: auto;
}

</style>
