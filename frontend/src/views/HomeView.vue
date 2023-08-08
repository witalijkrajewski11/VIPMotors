<template>
   <div class="container">
    <div class="columns is-multiline is-mobile">
      <div v-for="brand in brands" :key="brand.id" class="column is-6-mobile is-3-tablet">
        <div
            class="car-tile box"
            @click="handleTileClick(brand)"
            :style="getTileStyle(brand)"
        >
          <div class="car-image">
            <img :src="brand.image" alt="Car Image">
          </div>
          <div class="car-info">
            <div class="car-name">
              {{ brand.name }}
            </div>
            <div v-if="brand.special_offer_discount" class="sale-label">
              Save $500*
            </div>
          </div>
        </div>
      </div>
    </div>
     <div>*Vehicle incentives and rebates are programs made available by car manufacturers to encourage vehicle sales by providing consumers with cash allowances or favorable financing/lease rates. Incentives can vary by location, vehicle configuration, as well as the buyer's method of payment (cash purchase, financing, lease). Some incentives can be stacked with other incentive programs, and some have eligibility conditions that must be met to qualify. Additional incentives are sometimes targeted to customer segment groups like college graduates, military members, etc. Incentives are normally subject to change and governed by specific eligibility rules. Please see your local dealer for details on incentives that might be available to you.</div>
  </div>
</template>


<script>

import axios from "axios";

export default {
  name: 'HomeView',
  data() {
    return {
      brands: [],
    }
  },
  methods: {
    async getAllBrands() {
      await axios
          .get('api/car_brands/')
          .then(res => {
            console.log(res)
            this.brands = res.data
          })
          .catch(e => {
            console.log(e)
          })
    },
    handleTileClick(brand) {
      console.log(brand.name)
      this.$router.push({name: 'CarModels', query: {brand_name: brand.name}})
    },
    getTileStyle(brand) {
      return {
        background: brand.special_offer_discount ? "linear-gradient(135deg, #F1FAFA 20%, transparent 20%)" : "",
      };
    },
  },
  mounted() {
    this.getAllBrands()
  }
}
</script>

<style scoped lang="scss">
@import "bulma";
.container {
  padding: 20px;
  font-family: Radikal,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,Roboto,sans-serif;
}

.car-tile {
  cursor: pointer;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 213px;
  height: 120px;
  border-radius: 8px;
}

.car-tile:hover {
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);
}

.columns {
  margin-left: 15.25rem;
}

.car-image img {
  max-width: 150px;
  width: 40px;
  height: 40px;
  max-height: 100px;
}

.car-name {
  margin-top: 10px;
  font-size: 18px;
}

.sale-label {
  position: absolute;
  top: 15px;
  left: -6px;
  font-weight: bold;
  background-color: #F1FAFA;
  color: #04806D;
  padding: 7px;
  border-radius: 120px;
  transform: rotate(-45deg);
  font-size: 12px;
}

//.sale-text {
//  display: block;
//  position: absolute;
//  //top: 50%;
//  //left: 50%;
//  transform: translate(-50%, -50%) rotate(-45deg);
//  font-size: 12px;
//  font-weight: bold;
//  color: #04806D;
//}
</style>
