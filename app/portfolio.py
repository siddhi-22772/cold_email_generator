import pandas as pd
import chromadb
import uuid


class Portfolio:

    def __init__(self, file_path="app/resource/techstack_active_links.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        self.chroma_client = chromadb.PersistentClient(  # persistantcleint stoore data into pc and client store data into ram
            path="vectorstore"
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio"
        )

    def load_portfolio(self):

        if self.collection.count() == 0:

            for _, row in self.data.iterrows():

                self.collection.add(
                    documents=[str(row["Techstack"])],
                    metadatas=[
                        {
                            "links": str(row["Links"])
                        }
                    ],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):

        # Make sure skills is a list
        if isinstance(skills, str):
            skills = [skills]

        # Remove empty values
        skills = [
            str(skill).strip()
            for skill in skills
            if skill and str(skill).strip()
        ]

        # If no skills are available
        if not skills:
            return []

        results = self.collection.query(
            query_texts=skills,
            n_results=2
        )

        return results.get("metadatas", [])