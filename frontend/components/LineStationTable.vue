<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Line</th>
                <th scope="col">Station</th>
                <th scope="col">Position</th>
                <th scope="col">Notes</th>
                <th scope="col">Actions</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(lineStation, index) in lineStations">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ lineStation.line.name }}</td>
                <td>{{ lineStation.station.name }}</td>
                <td>{{ lineStation.order  }}</td>
                <td>{{ lineStation.notes }}</td>
                <td>
                    <button
                        class="btn btn-sm btn-primary me-2" 
                        data-bs-toggle="modal" 
                        data-bs-target="#editLineStationModal"
                        @click="selectLineStation(lineStation)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-line-station', lineStation)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Edit LineStation Modal -->
    <div class="modal fade" id="editLineStationModal" tabindex="-1" aria-labelledby="editLineStationModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="editLineStationModalLabel">Edit Line-Station</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="line" class="form-label">Line</label>
                        <select v-model="updatedLineStation.line" class="form-control" id="line">
                            <option v-for="line in lines" :value="line">{{ line.name }}</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="station" class="form-label">Station</label>
                        <select v-model="updatedLineStation.station" class="form-control" id="station">
                            <option v-for="station in stations" :value="station">{{ station.name }}</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="order" class="form-label">Position</label>
                        <input v-model="updatedLineStation.order" type="text" class="form-control" id="order">
                    </div>
                    <div class="mb-3">
                        <label for="notes" class="form-label">Notes</label>
                        <input v-model="updatedLineStation.notes" type="text" class="form-control" id="notes">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="$emit('edit-line-station', updatedLineStation)" data-bs-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        emits: ['delete-line-station', 'edit-line-station'],
        props: {
            lineStations: {
                type: Array,
                required: true
            },
            lines: {
                type: Array,
                required: true
            },
            stations: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                updatedLineStation: {
                    id: '',
                    line: '',
                    station: '',
                    order: '',
                    notes: '',
                }
            }
        },
        methods: {
            selectLineStation(lineStation) {
                this.updatedLineStation = { ...lineStation }
            },
        }
    }

</script>