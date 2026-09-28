from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model data mahasiswa
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# Database sementara (disimpan di memori)
mahasiswa_db = {}

@app.get("/")
def read_root():
    return {"message": "API Data Mahasiswa"}

# CREATE (POST): menambah data mahasiswa
@app.post("/mahasiswa/{id}")
def tambah_mahasiswa(id: int, data: Mahasiswa):
    if id in mahasiswa_db:
        raise HTTPException(status_code=400, detail="ID sudah dipakai")
    mahasiswa_db[id] = data.dict()
    return {"message": "Data berhasil ditambahkan", "data": mahasiswa_db[id]}

# READ (GET): melihat semua data mahasiswa
@app.get("/mahasiswa")
def lihat_semua_mahasiswa():
    return mahasiswa_db

# READ (GET): melihat satu data mahasiswa berdasarkan ID
@app.get("/mahasiswa/{id}")
def lihat_mahasiswa(id: int):
    if id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    return {"id": id, "data": mahasiswa_db[id]}

# UPDATE (PUT): mengubah data mahasiswa berdasarkan ID
@app.put("/mahasiswa/{id}")
def ubah_mahasiswa(id: int, data: Mahasiswa):
    if id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    mahasiswa_db[id] = data.dict()
    return {"message": "Data berhasil diubah", "data": mahasiswa_db[id]}

# DELETE: menghapus data mahasiswa berdasarkan ID
@app.delete("/mahasiswa/{id}")
def hapus_mahasiswa(id: int):
    if id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    data_terhapus = mahasiswa_db.pop(id)
    return {"message": "Data berhasil dihapus", "data": data_terhapus}