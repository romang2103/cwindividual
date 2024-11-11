<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Station</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(station, index) in stations">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ station.name }}</td>
                <td>
                    <button
                        class="btn btn-sm btn-primary me-2" 
                        data-bs-toggle="modal" 
                        data-bs-target="#editStationModal"
                        @click="selectStation(station)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-station', station)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Modal -->
    <div class="modal fade" id="editStationModal" tabindex="-1" aria-labelledby="editStationModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="editStationModalLabel">Add Station</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input v-model="updatedStation.name" type="text" class="form-control" id="name">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="$emit('edit-station', updatedStation)" data-bs-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        emits: ['delete-station', 'edit-station'],
        props: {
            stations: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                updatedStation: {
                    id: '',
                    name: '',
                }
            }
        },
        methods: {
            // Populate the updatedStation object with the selected station
            selectStation(station) {
                this.updatedStation = { ...station }
            },
        }
    }

</script>