import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

EXCEL_FILE = Path("du_lieu_nhap_xuat_dau.xlsx")
SHEET_NAME = "Du_lieu"

st.set_page_config(page_title="Nhập – Xuất dầu", layout="wide")
st.title("NHẬP – XUẤT DẦU")

st.write("Nhập dữ liệu mỗi ngày, hệ thống sẽ lưu và cộng dồn vào file Excel.")


def load_data():
    if EXCEL_FILE.exists():
        return pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    else:
        columns = [
            "Ngày",
            "Xuất",
            "Cây 1",
            "Cây 2",
            "Cây 3",
            "Nhập xe dầu di động",
            "Nhập Dầu khí Ninh Bình",
            "Nhập Hoàng Long",
            "Tồn thực tế đo cuối ngày bể dầu",
            "Tồn xe dầu di động cuối ngày",
            "Chênh lệch so với xe đo định mức 6449",
            "Tồn tính theo sổ sách",
            "Chênh lệch",
        ]
        return pd.DataFrame(columns=columns)


def append_and_save(df, new_row):
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)
    return df


df = load_data()

with st.expander("Xem dữ liệu đã lưu"):
    st.dataframe(df, use_container_width=True)

st.markdown("---")

st.subheader("Nhập dữ liệu ngày mới")

with st.form("form_nhap_du_lieu", clear_on_submit=True):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        ngay = st.date_input("Ngày", value=datetime.today())
        xuat = st.number_input("Xuất", min_value=0.0, step=0.001, format="%.3f")
        cay1 = st.number_input("Cây 1", min_value=0.0, step=0.001, format="%.3f")
    with col2:
        cay2 = st.number_input("Cây 2", min_value=0.0, step=0.001, format="%.3f")
        cay3 = st.number_input("Cây 3", min_value=0.0, step=0.001, format="%.3f")
        nhap_xe_di_dong = st.number_input(
            "Nhập xe dầu di động", min_value=0.0, step=0.001, format="%.3f"
        )
    with col3:
        nhap_ninh_binh = st.number_input(
            "Nhập Dầu khí Ninh Bình", min_value=0.0, step=0.001, format="%.3f"
        )
        nhap_hoang_long = st.number_input(
            "Nhập Hoàng Long", min_value=0.0, step=0.001, format="%.3f"
        )
        ton_thuc_te_be = st.number_input(
            "Tồn thực tế đo cuối ngày bể dầu",
            min_value=0.0,
            step=0.001,
            format="%.3f",
        )
    with col4:
        ton_xe_cuoi_ngay = st.number_input(
            "Tồn xe dầu di động cuối ngày",
            min_value=0.0,
            step=0.001,
            format="%.3f",
        )
        ton_so_sach = st.number_input(
            "Tồn tính theo sổ sách", min_value=0.0, step=0.001, format="%.3f"
        )
        chenh_lech_6449 = st.number_input(
            "Chênh lệch so với xe đo định mức 6449",
            value=0.0,
            step=0.001,
            format="%.3f",
        )

    chenh_lech = ton_thuc_te_be - ton_so_sach

    st.write(f"**Chênh lệch (Tồn thực tế - Tồn sổ sách): {chenh_lech:.3f}**")

    submitted = st.form_submit_button("Lưu vào Excel")

    if submitted:
        new_row = {
            "Ngày": ngay,
            "Xuất": xuat,
            "Cây 1": cay1,
            "Cây 2": cay2,
            "Cây 3": cay3,
            "Nhập xe dầu di động": nhap_xe_di_dong,
            "Nhập Dầu khí Ninh Bình": nhap_ninh_binh,
            "Nhập Hoàng Long": nhap_hoang_long,
            "Tồn thực tế đo cuối ngày bể dầu": ton_thuc_te_be,
            "Tồn xe dầu di động cuối ngày": ton_xe_cuoi_ngay,
            "Chênh lệch so với xe đo định mức 6449": chenh_lech_6449,
            "Tồn tính theo sổ sách": ton_so_sach,
            "Chênh lệch": chenh_lech,
        }

        df = append_and_save(df, new_row)
        st.success("Đã lưu dữ liệu vào file Excel thành công!")

        with st.expander("Xem bảng sau khi lưu", expanded=True):
            st.dataframe(df, use_container_width=True)
