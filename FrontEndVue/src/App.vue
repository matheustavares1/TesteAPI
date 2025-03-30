<template>
  <div class="container">
    <h2>Buscar Operadoras</h2>
    <input
        v-model="termo"
        type="text"
        placeholder="Digite o nome da operadora"
        @input="buscarOperadoras"
    />
    <ul v-if="resultados.length">
      <li v-for="(op, index) in resultados" :key="index">
        <strong>{{ op.Nome_Fantasia }}</strong> - {{ op.Cidade }} ({{ op.UF }}) CNPJ: {{ op.CNPJ}} ANS: {{op.Registro_ANS}}
      </li>
    </ul>
    <p v-else-if="termo">Nenhuma operadora encontrada.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termo: "",
      resultados: []
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termo.length < 2) {
        this.resultados = [];
        return;
      }
      try {
        const response = await axios.get("http://127.0.0.1:8000/buscar-operadoras", {
          params: { termo: this.termo }
        });
        this.resultados = response.data.resultados;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: auto;
  text-align: center;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background: #f4f4f4;
  padding: 8px;
  margin: 5px 0;
  border-radius: 5px;
}
</style>