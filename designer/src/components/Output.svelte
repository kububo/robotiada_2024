<script lang="ts">
  import { state } from "../state";

  let programOutput = "";

  $: programOutput = $state.shapes.map((shape) => shape.toProgram()).join("\n");
</script>

<div class="element">
  <div class="tooltip">
    <div>
      LINE <i>délka</i>
    </div>
    <div>
      ARC <i>poloměr délka</i>
    </div>
  </div>

  <textarea value={programOutput} rows="10" cols="100" readonly></textarea>
</div>

<style>
  .element {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .tooltip {
    display: inline-block;
    padding: 1rem;
    border: 1px solid lightskyblue;
    border-radius: 1rem;
  }
</style>
